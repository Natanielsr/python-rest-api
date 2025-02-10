import os

class FolderInfo:
    """Classe para obter informações sobre uma pasta."""
    
    def __init__(self, folder_path):
        self.folder_path = folder_path
    
    def get_info(self):
        """Retorna a quantidade de arquivos e o tamanho total da pasta."""
        total_size = 0
        file_count = 0
        
        for root, _, files in os.walk(self.folder_path):
            file_count += len(files)
            for file in files:
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)
        
        return file_count, total_size

if __name__ == "__main__":
    folder_path = './slide_file'
    folder_info = FolderInfo(folder_path)
    files, size = folder_info.get_info()
    print(f"Arquivos: {files}")
    print(f"Tamanho total: {size / (1024 * 1024):.2f} MB")