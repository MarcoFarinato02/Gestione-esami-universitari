import socket
import pickle

class UniversityServer:
    def _init_(self):
        self.exams = []


    def save_exam(self,exam_name, exam_date):
        print("in save_exam "+str(exam_name))
        with open('exams.txt', 'a') as file:
            file.write(f'{exam_name} {exam_date}\n')

    def save_reservation(self):
        print ('In save_reservation\n')
        with open('confirmedReservation.txt', 'a') as file:
            with open('prenotazioni.txt', 'a+') as temp_f:
                temp_f.seek(0)
                datafile = temp_f.readlines()
                for line in datafile:
                    file.write(f'{line}\n')
                    print (line)

            temp_f.close()
        file.close()
        with open('prenotazioni.txt', 'a+') as temp_f:                 
            temp_f.seek(0)
            temp_f.truncate()        
        
 
    def handle_reservation(self, exam_name):
        available_exams = [exam for exam in self.exams if exam['name'] == exam_name]
        if available_exams:
            return available_exams[0]['dates']
        else:
            return "Exam not found."

def main():
    server = UniversityServer()
    host = '127.0.0.1'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()

        print(f"University server listening on {host}:{port}")

        while True:
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                data = conn.recv(1024)
                if not data:
                    break
                data = pickle.loads(data)
                if data['action'] == 'add_exam':
                    print('request from secretary...')
                    exam=data['exam']
                    exam_name=exam['name']
                    exam_date=exam['dates']
                    server.save_exam(exam_name,exam_date)
                    conn.send("Exam added successfully.".encode('utf-8'))
                    print('sent respons to secretary for exam added...')
                elif data['action'] == 'reserve_exam':
                    print('request from secretary to reserve all student request...')
                    server.save_reservation()
                    conn.send("Reservation done...".encode('utf-8'))
                    print('sent respons to secretary for all reservation...')



if __name__ == "__main__":
    main()