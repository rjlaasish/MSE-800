

class FileOperation:
    
    def __init__(self, file_path,mode):
        self.filePath = file_path
        self.mode = mode
        
    def open_file(self):
        file = open(self.filePath, self.mode)
        print(f"File '{self.filePath}' opened in '{self.mode}' mode.")
        return file
    
    def read_file(self):
        data = open(self.filePath,mode=self.mode)
        lines = data.readlines() 
        for line in lines:
            print(line[:]) 
        data.close()
    
    def write_file(self,write_content):
        with open(self.filePath,self.mode) as file:
            file.write(write_content)
            file.close()
        print("Content written to file successfully.")
        
    def count_words_in_file(self):
        with open(self.filePath,self.mode) as file:
            content = file.read()
            words = content.split()
            print(f"Total words in your file is: {len(words)}")
            file.close()
        
        

    
def main():
    file_path = input("Enter the file path: ")
    print("Choose an operation:")
    print("1. Open File")
    print("2. Read File")
    print("3. Write to File")
    print("4. Count words in file")
    
    choice = int(input("Enter your choice (1/2/3/4): \n"))
    
    mode = 'r' if choice in [1, 2, 4] else 'w'
    
    file_op = FileOperation(file_path, mode)
    
    
    match choice:
        case 1:
            file = file_op.open_file()
            if file:
                file.close()
        case 2:
            file_op.read_file()
        case 3:
            content = input("Enter content to write to the file: ")
            file_op.write_file(content)
        case 4:
            file_op.count_words_in_file()
        case _:
            print("Invalid choice. Please select 1, 2, or 3.")

    
    
if __name__ == "__main__":
    main()
    