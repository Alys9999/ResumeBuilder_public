Resume Project Generator

This repository provides a workflow to automatically generate a tailored resume in .docx format. By maintaining a project bank and processing each job description (JD), the script extracts the relevant skills and selects the top three projects to highlight.

Workflow

Prepare Project Bank
Maintain your project details in a structured format. Each time you input a new JD, the script will select the most relevant skills and projects.

Format Skills
Skills are grouped into categories and listed as tuples:

skills = [
    ("Frontend Development:",  "React Native, Flutter, TypeScript/JavaScript, HTML/CSS"),
    ("Backend Development:",   "Python, C, C++, Node.js, Data Structures & Algorithms, Distributed Systems"),
    ("Systems & OS:",          "Linux, Linux Kernel Development, Multithreading/Processes, Sockets (TCP/UDP), Bash/Shell"),
    ("Database & Cloud:",      "MongoDB, Firebase, Redis, AWS ECS, Linear Programming, Resource Optimization"),
    ("Development Tools:",     "Git, REST APIs, Stripe API, Google Maps API, Make/CMake"),
    ("Relevant Courses:",      "Systems Programming (Linux), Computer Architecture"),
]


Format Projects
Projects are stored in a list of tuples, where each project contains a title/time and a list of descriptions:

projects = [
    (
        "Project Title | Time Period",
        [
            "Description 1",
            "Description 2",
        ],
    ),
]


Run Resume Generator
Insert your skills and projects into create_resume.py, then execute:

python create_resume.py


This will generate a .docx file containing your customized resume.

Finalize Resume
Open the generated .docx.
Make manual adjustments as needed.
Save/export the final version as .pdf for submission.

Notes

Keep your project bank updated for reuse across different applications.

Modify skill categories or add new sections in create_resume.py as required.

The .pdf output should always be reviewed before sending out applications.