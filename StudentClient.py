import socket
import pickle

class StudentClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def inquire_exam_dates(self, exam_name):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            data = {'action': 'inquire_exam_dates', 'exam_name': exam_name}
            s.sendall(pickle.dumps(data))
            response = s.recv(1024)
            print(response)
 
    def reserve_exam(self, reservation):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            data_reservation = {'action': 'save_reservation', 'reservation': reservation}
            s.sendall(pickle.dumps(data_reservation))
            response = s.recv(1024)
            print(response)

def main():

    student = StudentClient('127.0.0.1', 54321)

    scelta=-1
    while(scelta != 0):
        print("""
        1.Inquire exam date
        2.Reserve exam
        3.Exit/Quit
        """)
        scelta = int(input("Insert number of your choice: "))

        if scelta==1:
            exam_name=str(input("Exam to search: "))
            available_dates = student.inquire_exam_dates(exam_name)
      
        elif scelta==2:
            print("\n Reserve exam")
            exam_name=str(input("Exam Name: "))
            date=str(input("Exam Date: "))
            name=str(input("Name: "))
            surname=str(input("Surname: "))
            matricola=str(input("Matricola: "))
            reservation = {'exam': exam_name, 'date': date, 'studentN': name, 'studentS': surname, 'Matricola': matricola}
            student.reserve_exam(reservation)
        elif scelta==3:
            print("\n Goodbye") 
            break
        else:
            print("\n Not Valid Choice Try again")
       


if __name__ == "__main__":
    main()
