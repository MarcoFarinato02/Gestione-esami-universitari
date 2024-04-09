import socket
import pickle

class SecretaryClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
       

    def add_exam(self, exam):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            data_exams = {'action': 'add_exam', 'exam': exam}
            s.sendall(pickle.dumps(data_exams))
            response = s.recv(1024)
            print(response)
           
    def reserve_all_exam(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            data = {'action': 'reserve_exam'}
            s.sendall(pickle.dumps(data))
            response = s.recv(1024).decode("utf-8", "ignore")
            print(response)


            
def main():

    
    secretaryclient = SecretaryClient('127.0.0.1', 12345)
    scelta=-1
    while(scelta != 0):
        print("******Secretary section******")
        print("      1. Add exam")
        print("      2. reserve student exams")
        print("      3. quit")
        scelta = int(input("Insert number of your choice: "))
        if scelta == 1:
        # Esempio di utilizzo:
            esame_da_inserire = str(input("Digit exam to insert: "))
            data1=str(input("First date  "))
            data2=str(input("Second date "))
            #exam = {'name': 'Math', 'dates': ['2024-03-10', '2024-03-15']}
            exam = {'name': esame_da_inserire, 'dates': [data1, data2]}
            secretaryclient.add_exam(exam)
        elif scelta == 2:
            #exam_name = str(input("Digit exam to reserve: "))
            #exam_name = 'Math'
            secretaryclient.reserve_all_exam()
        elif scelta == 3:
            print("*** Bye....")
            break
        else:
            print("Not valid choice. Insert 1 or 2 or 3.")



if __name__ == "__main__":
    main()
