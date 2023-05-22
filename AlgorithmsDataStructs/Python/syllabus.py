print("""*-----------------------------------------*
| |
| Welcome to the Syllabus Viewer! |
| |
*-----------------------------------------*
Version 1

-----Information-----
"Year" refers to the school year the class was conducted.
Type "2020" for June 2020-May 2021.
Type "2021" for June 2021-May 2022.
Type "2022" for June 2022-May 2023, etc.

"Semester" refers to the semester the class was conducted.
Type "0" for Intersession (June-July)
Type "1" for First Semester (August-December)
Type "2" for Second Semester (January-May)
""")

def paste():
    global z
    global i

print("""
--- Class {0} ---""".format(i+1))
source = input("""
Source:
""")
while source != "A" and source != "B":
    source = input("""
    You have entered an invalid response.
    Source:
    """)
    if source == "A":
        z = input("""
        Whole Row in AISIS:
        """)
        z = z.split(chr(9))
    else:
        z = input("""
        Whole Row in AISIS:
        """)
        z = z.split(chr(9))
        z.insert(5,"Modality")

def view():
 global year
 global semester
 global dept_code
 global course_code
 global prof
 global prof_first
 global prof_last
 global section
 global link

 year = input("""
Year:
""")
 semester = input("""
Semester:
""")
 semester = semester[0]

 code = {"BIO": "BIO", "BIOED": "BIO", "SCIED": "BIO", "CHEM": "CH", "MATSE": "CH", "CHEMED": "CH",
 "CSP": "CHN", "COM": "COM", "COMM": "COM", "JRN": "COM", "CPA": "CPA", "EDUC": "CPA",
 "ELM": "ELM", "DEV": "DS", "ECON": "EC", "EDCSP": "ED", "CE": "ECE", "CIE": "ECE",
 "ELC": "ECE", "ENGG": "ECE", "ENGSCI": "ECE", "ENE": "EN", "ENGL": "EN", "ENLIT": "EN",
 "ENLL": "EN", "DIRR": "ES", "ENVI": "ES", "MEM": "ES", "EURO": "EU", "FILI": "FIL",
 "PNTKN": "FIL", "ACCT": "FAA", "FINN": "FAA", "ARTM": "FA", "ARTS": "FA", "CRWR": "FA",
 "FA": "FA", "FA-ID": "FA", "IDES": "FA", "THTR": "FA", "HSCI": "HSP", "HISTO": "HI",
 "ArtAp": "SOHUM", "DLQ": "SOHUM", "CS": "DISCS", "CSCI": "DISCS", "GDEV": "DISCS","ISCS": "DISCS",
 "MSYS": "DISCS", "INTACT": "INTAC", "HUMAN": "IS", "IDS": "IS", "JPN": "JSP", "KOR": "KSP",
 "KRN": "KSP", "LAS": "LAS", "SOMGT": "LAS", "LLAW": "MAL", "MKTG": "MAL", "MATH": "MA",
 "MTHED": "MA", "FRE": "ML", "GER": "ML", "ITA": "ML", "PORT": "ML", "RUSS": "ML",
 "SPA": "ML", "PHILO": "PH", "PHYED": "PE", "ATMOS": "PS", "PHYS": "PS", "PHYSE": "PS",
 "POLSC": "POS", "POSPM": "POS", "SEAS": "POS", "LEAD": "PSY", "PSYC": "PSY", "DECSC": "QMIT",
 "DECSCI": "QMIT", "ITENT": "QMIT", "ITMGT": "QMIT", "OPMAN": "QMIT", "QUANT": "QMIT","STS": "SB",
 "SocSc": "SOCSCI", "ANTH": "SA", "SOAN": "SA", "SOCDV": "SA", "SOCIO": "SA", "RELED": "TH",
 "THEO": "TH", "TMP": "TMP", "TMPSS": "TMP"}

 old_code = ["BIO","CH","CHN","COM","CEPP","CPA","ELM","DS","EC","ED",
 "ECE","EN","ES","EU","FIL","FAA","FA","HSP","HI","SOHUM",
 "DISCS","INTAC","IS","JSP","KSP","LAS","MAL","MA","ML","NSTP (ADAST)",
 "NSTP (OSCI)","PH","PE","PS","POS","PSY","QMIT","SB","SOCSCI","SA",
 "TH","TMP"]
 
 if z[0] == "NSTP 11(CWTS)" or z[0] == "NSTP 12(CWTS)":
 dept_code = "NSTP (OSCI)"
 elif z[0] == "NSTP 11(ROTC)" or z[0] == "NSTP 12(ROTC)":
 dept_code = "NSTP (ADAST)"
 elif z[0].split()[0] in old_code:
 dept_code = z[0].split()[0]
 else:
 dept_code = code[z[0].split()[0]]

 course_code_spaced = z[0].split()
 course_code = ""
 for i in range(len(course_code_spaced)):
 course_code += course_code_spaced[i]

 comma_count = 0
 for i in range(len(z[6])):
 if z[6][i] == ",": comma_count += 1
 if comma_count == 1:
 prof_first = z[6].split(", ")[0]
 prof_last = z[6].split(", ")[1][0]
 prof = prof_first + "_" + prof_last
 elif comma_count == 2:
 prof = z[6].split(", ")
 if prof[1] in ["Jr.", "JR.", "Jr", "JR", "SJ", "S.J."]:
 prof[0] = prof[0] + ", " + prof[1]
 prof.remove(prof[1])
 prof_first = prof[0]
 prof_last = prof[1][0]
 prof = prof_first + "_" + prof_last
 elif comma_count % 2 == 1:
 prof_count = comma_count // 2 + 1
 profs = z[6].split(", ")
 print(profs)
 prof = ""
 for i in range(prof_count):
 prof_first = z[6].split(", ")[2*i]
 prof_last = z[6].split(", ")[2*i+1][0]
 prof += prof_first
 prof += "_"
 prof += prof_last
 prof += "_"
 prof = prof[:-1]
 else:
 print("This class likely has many professors, and at least one has Jr./SJ. Not supported as of now")
 
 section = z[1]
 
 if comma_count >=1 :
 link = "aisis.ateneo.edu/syllabi/{0}/{1}/CS-{2}-{3}-{4}-{5}-{0}-{1}.pdf".format(
 year,semester,dept_code,course_code,prof,section)
 else:
 link = "The link cannot be generated because there seems to be no professors."

number = input("""How many class syllabi do you want to check?
""")
try: number = int(number)
except:
 while type(number) != int:
 number = input("""
You have entered an invalid response, please input a number.
How many class syllabi do you want to check?
""")
 try: number = int(number)
 except: pass
 
total = ""
for i in range(number):
 paste()
 view()
 total += link
 total += "\n"

print("""
Here is/are the class syllabus/i you requested:

{}
Thank you for using the Syllabus Viewer!""".format(total))
