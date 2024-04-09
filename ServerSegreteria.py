import socket
import pickle

class ServerSegreteria:
    def __init__(self):
        self.exams = []


    def save_reservation(self, exam_name, exam_date, student_name, student_surname, student_matricola):
        print("in reservation_secretary "+str(student_name))
        with open('prenotazioni.txt', 'a') as file:
            file.write(f'{exam_name} {exam_date} {student_name} {student_surname} {student_matricola}\n')

    def handle_reservation(self, exam_name):
        with open('exams.txt') as temp_f:
          datafile = temp_f.readlines()
        available_exams = '00.00.0000'
        for line in datafile:
          #print("leggo "+line)
          if exam_name in line:
            available_exams = line  # The string is found
            print (available_exams)
            break
 
        if available_exams:
            return available_exams
        else:
            return "Exam not found."

def main():
    server = ServerSegreteria()
    host = '127.0.0.1'
    port = 54321

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()

        print(f"Secretary server listening on {host}:{port}")

        while True:
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                data = conn.recv(1024)
                if not data:
                    break
                data = pickle.loads(data)
                if data['action'] == 'save_reservation':
                    print('request save_reservation from student...')
                    reservation=data['reservation']
                    exam_name=reservation['exam']
                    print(exam_name)
                    exam_date=reservation['date']
                    print(exam_date)
                    student_name=reservation['studentN']
                    print(student_name)
                    student_surname=reservation['studentS']
                    print(student_surname)
                    student_matricola=reservation['Matricola']
                    print(student_matricola)
                    server.save_reservation(exam_name,exam_date,student_name,student_surname,student_matricola)
                    conn.send("Reservation added successfully.".encode('utf-8'))
                    print('sent respons to student for reservation added...')
                elif data['action'] == 'inquire_exam_dates':
                    print('request from student...TO be implement')
                    print('request from student...inquiry date for '+data['exam_name'])
                    response = server.handle_reservation(data['exam_name'])
                    conn.sendall(str(response).encode())



if __name__ == "__main__":
    main()
