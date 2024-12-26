import numpy as np

class File:
    def __init__(self, file_id, size):
        self.file_id = file_id
        self.size = size
        self.start_block = None
        self.end_block = None

def contiguous_allocation(files, total_blocks):
    allocation = np.full(total_blocks, -1)  # -1 indicates free block
    allocation_table = []

    for file in files:
        found = False

        # Try to find contiguous blocks
        for i in range(total_blocks - file.size + 1):
            if np.all(allocation[i:i + file.size] == -1):
                file.start_block = i
                file.end_block = i + file.size - 1
                allocation[i:i + file.size] = file.file_id
                found = True
                allocation_table.append((file.file_id, i, i + file.size - 1))  # (file_id, start_block, end_block)
                break

        if not found:
            allocation_table.append((file.file_id, -1, -1))  # File couldn't be allocated

    return allocation, allocation_table

def linked_allocation(files, total_blocks):
    allocation = np.full(total_blocks, -1)  # -1 indicates free block
    allocation_table = []
    free_list = list(range(total_blocks))  # List of free blocks

    for file in files:
        if len(free_list) < file.size:
            allocation_table.append((file.file_id, -1))  # Not enough space for this file
            continue

        file.start_block = free_list[0]  # Allocate the first available block
        current_block = file.start_block
        allocation[file.start_block] = file.file_id

        for i in range(1, file.size):
            next_block = free_list[i]
            allocation[current_block] = next_block
            current_block = next_block

        allocation[current_block] = -1  # Mark the end of linked blocks
        allocation_table.append((file.file_id, file.start_block))  # Start block of this file
        del free_list[:file.size]  # Remove allocated blocks from free list

    return allocation, allocation_table

def print_allocation(allocation, title):
    print(f"\n{title}")
    print("Block Index: ", end='')
    for index in range(len(allocation)):
        print(f"{index:3}", end=' ')
    print()

    print("File ID:    ", end='')
    for block in allocation:
        print(f"{block if block != -1 else ' ' :3}", end=' ')
    print("\n")

def main():
    try:
        total_blocks = int(input("Enter the total number of disk blocks: "))
        if total_blocks <= 0:
            raise ValueError("Total blocks must be a positive integer.")
        
        num_files = int(input("Enter the number of files: "))
        if num_files <= 0:
            raise ValueError("Number of files must be a positive integer.")

        files = []

        for i in range(num_files):
            size = int(input(f"Enter size of file {i + 1} (in blocks): "))
            if size <= 0:
                raise ValueError("File size must be a positive integer.")
            files.append(File(i + 1, size))

        # Using Contiguous Allocation
        print("\n--- Contiguous Allocation ---")
        contiguous_allocation_table = contiguous_allocation(files, total_blocks)
        print_allocation(contiguous_allocation_table[0], 'Contiguous Allocation')
        print("Allocation table (File ID, Start Block, End Block):")
        print(contiguous_allocation_table[1])

        # Using Linked Allocation
        print("\n--- Linked Allocation ---")
        linked_allocation_table = linked_allocation(files, total_blocks)
        print_allocation(linked_allocation_table[0], 'Linked Allocation')
        print("Allocation table (File ID, Start Block):")
        print(linked_allocation_table[1])

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
