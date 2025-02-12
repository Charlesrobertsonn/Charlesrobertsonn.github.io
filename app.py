from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def registration_form():
    return render_template_string(open('registration.html').read())

@app.route('/register', methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    
    # Save the registration data to a file (e.g., registrations.txt)
    with open('registrations.txt', 'a') as file:
        file.write(f'{first_name},{last_name},{email},{password}\n')
    
    return 'Registration successful!'

if __name__ == '__main__':
    app.run(debug=True)
