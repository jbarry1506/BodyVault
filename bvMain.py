import tkinter as tk
from tkinter import *
from tkinter import ttk
import json


class myApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "test windows")
        self.geometry('700x700+500+50')

        mainwin = ttk.Panedwindow(self, orient="horizontal")
        mainwin.pack(fill="both", expand=True)

        # splash page
        splashPage = ttk.Frame(mainwin, width=700, height=700, relief="sunken")

        # login page
        loginPage = ttk.Frame(mainwin, width=700, height=700, relief="sunken")

        # left side of entry page
        entryPage = ttk.Frame(mainwin, relief="sunken")
        # right side of entry page
        entryPage2 = ttk.Frame(mainwin, relief="sunken")
        # right side
        subwin1 = ttk.Panedwindow(entryPage2, orient="vertical")
        subwin1.pack(fill="both", expand=True)
        # right side - inside top
        subentryPage = ttk.Frame(subwin1, relief="sunken")
        # right side - inside bottom
        subentryPage2 = ttk.Frame(subwin1, relief="sunken")

        # graphPage
        graphPage = ttk.Frame(mainwin, width=900, height=700, relief="sunken")

        # globals
        sexvar = "No Sex"
        heightvar = StringVar()
        heightvar.set("inches")
        weightvar = StringVar()
        weightvar.set("pounds")

        def lbm():
            print("Calculating")
            weight_lbs = float(weightLbsEntry.get())
            body_fat = float(bodyfatEntry.get())
            lean_body_mass = weight_lbs - (weight_lbs * (body_fat / 100))
            print(lean_body_mass)
            lbmlabel2.configure(text=lean_body_mass)
            lbmlabel1.grid(padx=10, pady=10, column=0, row=0)
            lbmlabel2.grid(padx=10, pady=10, column=1, row=0)
            hidebutton.grid(padx=10, pady=10, column=1, row=2)

        def hidelabel():
            print("Hide Label Pressed")
            lbmlabel2.grid_forget()
            graphwindow()

        def heightfunc(*args):
            height = heightvar.get()
            if height == "centimeters":
                print(height)
                centEntry.state(["!disabled"])
                feetEntry.state(["disabled"])
                inchesEntry.state(["disabled"])
            elif height == "inches":
                print(height)
                centEntry.state(["disabled"])
                feetEntry.state(["!disabled"])
                inchesEntry.state(["!disabled"])
            else:
                print(height)
                centEntry.state(["!disabled"])
                feetEntry.state(["!disabled"])
                inchesEntry.state(["!disabled"])

        def weightfunc(*args):
            weight = weightvar.get()
            if weight == "kilograms":
                print("Weight kilograms" + weight)
            elif weight == "pounds":
                print("Weight pounds" + weight)

        def heightcalc():
            feet = int(feetEntry.get())
            inches = int(inchesEntry.get())
            centimeters = int(centEntry.get())
            if feet != 0:
                feettemp = (feet * 12) + inches
                centimeters = feettemp * 2.54
                print(centimeters)
                centEntry.state(["!disabled"])
                centEntry.delete(0, END)
                centEntry.insert(0, str(int(centimeters)))
                centEntry.state(["disabled"])
                htCmLabel2.configure(text=str(int(centimeters)))
                htCmLabel1.grid(padx=10, pady=10, column=0, row=1)
                htCmLabel2.grid(padx=10, pady=10, column=1, row=1)
            elif centimeters != 0:
                print("Centimeters = " + str(centimeters))
                inchesTemp = centimeters / 2.54
                feet = int(inchesTemp / 12)
                inches = inchesTemp - (feet * 12)
                print("feet = " + str(feet))
                feetEntry.state(["!disabled"])
                feetEntry.delete(0, END)
                feetEntry.insert(0, str(feet))
                feetEntry.state(["disabled"])
                htFtLabel2.configure(text=str(int(feet)))
                htFtLabel1.grid(padx=10, pady=10, column=0, row=1)
                htFtLabel2.grid(padx=10, pady=10, column=1, row=1)
                print("inches = " + str(round(inches)))
                inchesEntry.state(["!disabled"])
                inchesEntry.delete(0, END)
                inchesEntry.insert(0, str(round(inches)))
                inchesEntry.state(["disabled"])
                htInLabel2.configure(text=str(round(inches)))
                htInLabel1.grid(padx=10, pady=10, column=0, row=2)
                htInLabel2.grid(padx=10, pady=10, column=1, row=2)

        def calculations():
            lbm()
            heightcalc()

        def allusers():
            with open("users.json", "r") as f:
                data = json.load(f)
            keylist = []
            for i in data:
                keylist.insert(0, i)
            return (keylist)

        def defineuser(s_user):
            userlist = allusers()
            selecteduser = s_user
            for i in userlist:
                if selecteduser == i:
                    print(selecteduser)
            entrywindow(selecteduser)

        def splashwindow():
            self.splashimage = PhotoImage(
                file="art/test-bank-vault-door.pgm")
            mainwin.add(splashPage, weight=1)
            splashPage.pack()
            splashlabel = ttk.Label(splashPage, text="Image here")
            splashlabel.pack()
            entryButton = ttk.Button(splashPage, text="Click Here to Unlock Your Potential", command=loginwindow)
            entryButton.pack()
            entryButton.place(x=250, y=340)
            splashlabel.config(image=self.splashimage)

        def loginwindow():
            self.splashimage = PhotoImage(
                file="art/test-bank-vault-door.pgm")
            entryPage.pack_forget()
            graphPage.pack_forget()
            splashPage.pack_forget()
            mainwin.add(loginPage, weight=1)
            splashlabel = ttk.Label(loginPage, text="Image here")
            splashlabel.pack()
            splashlabel.config(image=self.splashimage)
            userLabel = ttk.Label(loginPage, text="                Users")
            userLabel.place(x=280, y=330)
            userLabel.configure(width=23, border=2)
            selected = StringVar()
            userSelect = ttk.Combobox(loginPage, textvariable=selected)
            userSelect.config(values=allusers())
            userSelect.place(x=280, y=350)
            loginButton = ttk.Button(loginPage, text="Login", command=lambda: defineuser(selected))
            loginButton.place(x=280, y=380)
            loginButton = ttk.Button(loginPage, text="New User", command=lambda: defineuser(selected))
            loginButton.place(x=360, y=380)

        def entrywindow(*args):
            graphPage.pack_forget()
            splashPage.pack_forget()
            mainwin.remove(loginPage)
            mainwin.add(entryPage, weight=1)
            mainwin.add(entryPage2, weight=1)
            subwin1.add(subentryPage, weight=1)
            subwin1.add(subentryPage2, weight=1)

        def graphwindow():
            splashPage.pack_forget()
            entryPage.pack_forget()
            graphPage.pack()

        splashwindow()

        # sex radio button
        sexLabel = ttk.Label(entryPage, text="Sex")
        sexMale = ttk.Radiobutton(entryPage, text="Male", variable=sexvar, value="Male")
        sexFemale = ttk.Radiobutton(entryPage, text="Female", variable=sexvar, value="Female")
        # name
        firstLabel = ttk.Label(entryPage, text="First Name")
        firstEntry = ttk.Entry(entryPage)
        lastLabel = ttk.Label(entryPage, text="Last Name")
        lastEntry = ttk.Entry(entryPage)
        # age
        ageLabel = ttk.Label(entryPage, text="Age")
        ageEntry = ttk.Entry(entryPage)
        # height
        heightLabel = ttk.Label(entryPage, text="Height")
        heightCM = ttk.Radiobutton(entryPage, text="Centimeters", variable=heightvar, value="centimeters",
                                   command=heightfunc)
        heightIN = ttk.Radiobutton(entryPage, text="Feet and Inches", variable=heightvar, value="inches",
                                   command=heightfunc)
        feetLabel = ttk.Label(entryPage, text="Height Feet")
        feetEntry = ttk.Entry(entryPage)
        inchesLabel = ttk.Label(entryPage, text="Height Inches (remainder)")
        inchesEntry = ttk.Entry(entryPage)
        centLabel = ttk.Label(entryPage, text="Height Centimeters")
        centEntry = ttk.Entry(entryPage)
        # weight
        weightLabel = ttk.Label(entryPage, text="Weight")
        weightKG = ttk.Radiobutton(entryPage, text="Kilograms", variable=weightvar, value="kilograms",
                                   command=weightfunc)
        weightLB = ttk.Radiobutton(entryPage, text="Pounds", variable=weightvar, value="pounds", command=weightfunc)
        weightKgsLabel = ttk.Label(entryPage, text="Weight KGs")
        weightKgsEntry = ttk.Entry(entryPage)
        weightLbsLabel = ttk.Label(entryPage, text="Weight Lbs")
        weightLbsEntry = ttk.Entry(entryPage)
        bodyfatLabel = ttk.Label(entryPage, text="Body Fat %")
        bodyfatEntry = ttk.Entry(entryPage)

        # Entry Field Map
        # sex
        sexLabel.grid(padx=20, pady=10, column=0, row=0, columnspan=2)
        sexMale.grid(padx=20, pady=10, column=0, row=1)
        sexFemale.grid(padx=20, pady=10, column=1, row=1)
        # name
        firstLabel.grid(sticky="W", padx=20, pady=10, column=0, row=2)
        firstEntry.grid(sticky="W", padx=20, pady=10, column=1, row=2)
        lastLabel.grid(sticky="W", padx=20, pady=10, column=0, row=3)
        lastEntry.grid(sticky="W", padx=20, pady=10, column=1, row=3)
        # age
        ageLabel.grid(sticky="W", padx=20, pady=10, column=0, row=4)
        ageEntry.grid(sticky="W", padx=20, pady=10, column=1, row=4)
        # height
        heightLabel.grid(padx=20, pady=10, column=0, row=5, columnspan=2)
        heightCM.grid(padx=20, pady=10, column=0, row=6)
        heightIN.grid(padx=20, pady=10, column=1, row=6)
        feetLabel.grid(sticky="W", padx=20, pady=10, column=0, row=7)
        feetEntry.grid(sticky="W", padx=20, pady=10, column=1, row=7)
        feetEntry.insert(0, '0')
        inchesLabel.grid(sticky="W", padx=20, pady=10, column=0, row=8)
        inchesEntry.grid(sticky="W", padx=20, pady=10, column=1, row=8)
        inchesEntry.insert(0, '0')
        centLabel.grid(sticky="W", padx=20, pady=10, column=0, row=9)
        centEntry.grid(sticky="W", padx=20, pady=10, column=1, row=9)
        centEntry.insert(0, '0')
        # weight
        weightLabel.grid(padx=20, pady=10, column=0, row=10, columnspan=2)
        weightKG.grid(padx=20, pady=10, column=0, row=11)
        weightLB.grid(padx=20, pady=10, column=1, row=11)
        weightKgsLabel.grid(sticky="W", padx=20, pady=10, column=0, row=12)
        weightKgsEntry.grid(sticky="W", padx=20, pady=10, column=1, row=12)
        weightKgsEntry.insert(0, '0')
        weightLbsLabel.grid(sticky="W", padx=20, pady=10, column=0, row=13)
        weightLbsEntry.grid(sticky="W", padx=20, pady=10, column=1, row=13)
        weightLbsEntry.insert(0, '0')
        bodyfatLabel.grid(sticky="W", padx=20, pady=10, column=0, row=14)
        bodyfatEntry.grid(sticky="W", padx=20, pady=10, column=1, row=14)
        bodyfatEntry.insert(0, '0')

        heightfunc()

        # Menubar
        mainwin.option_add("*tearOff", False)
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        file = tk.Menu(menubar)
        menubar.add_cascade(menu=file, label="File")
        file.add_command(label='New', command=lambda: print("New Entry"))

        # Dynamic Labels and Buttons
        lbmlabel1 = ttk.Label(subentryPage, text="Lean Body Mass:  ")
        lbmlabel2 = ttk.Label(subentryPage)
        htCmLabel1 = ttk.Label(subentryPage, text="Centimeters:  ")
        htCmLabel2 = ttk.Label(subentryPage)
        htFtLabel1 = ttk.Label(subentryPage, text="Feet:  ")
        htFtLabel2 = ttk.Label(subentryPage)
        htInLabel1 = ttk.Label(subentryPage, text="Inches:  ")
        htInLabel2 = ttk.Label(subentryPage)
        hidebutton = ttk.Button(subentryPage2, text="Hide Label", command=hidelabel)

        # heightCM.bind("<ButtonPress>", heightfunc)
        # heightIN.bind("<ButtonPress>", heightfunc)
        button1 = ttk.Button(subentryPage2, text="Calculate", command=calculations)
        button1.grid(padx=10, pady=10, column=1, row=1)


app = myApp()
app.mainloop()


"""
This code is from my MacroFit web app
//MacroFit calculations
$sex = radioSelected(document.getElementsByName('sx')); //male or female
$age = 0; //age
$height = 0; //inches
$feetField = 0; //feet to be converted
$inchesField = 0; //inches
$centField = 0; //centimeters
$weightlbs = 0; //lbs
$weightKilos = 0; //kilograms
$bodyFat = 0; //body fat percentage
$actLevel = 0; //activity level 1-5
$bmr = 0; //basal metabolic rate
$tdee = 0; //total daily energy expendature

//functions

function resetForm(){
    document.getElementById('basicStatsHT').reset();
    document.getElementById('basicStatsWT').reset();
    document.getElementById('bflbm').reset();
    document.getElementById('SexAgeActivity').reset();
}

//converts height from feet and inches to centimeters, centimeters to feet and inches
function heightCalc($feetField, $inchesField, $centField) {
    $feetField = +document.getElementById('ft').value;
    $inchesField = +document.getElementById('in').value;
    $centField = +document.getElementById('cm').value;
    if ($feetField != 0) {
        $ifTemp = ($feetField * 12)+$inchesField;
        $centField = (2.54*$ifTemp).toFixed(0);
        document.getElementById("cm").value=$centField;
    }
    else if ($feetField == 0 && $inchesField == 0 && $centField != 0){
        $ifTemp = $centField / 2.54;
        $feetField = ($ifTemp / 12).toFixed(0);
        $feetInches = ($feetField * 12);
        $inchesField = Math.round(($ifTemp - $feetInches)/2.54);
        document.getElementById("ft").value=$feetField;
        document.getElementById("in").value=$inchesField; 
    }
    else {
        document.getElementById("heightout").innerHTML = "Please enter a value";
    }
}

//converts kilograms to lbs, lbs to kilograms
function weightCalc($weightKilos, $weightlbs) {
    $weightKilos = +document.getElementById("kg").value;
    $weightlbs = +document.getElementById("lbs").value;
    if ($weightKilos == 0 && $weightlbs != 0){
        $lbsTemp = $weightlbs / 2.20462262;
        document.getElementById("kg").value = $lbsTemp;
    }
    else if ($weightKilos != 0 && $weightlbs == 0){
        $lbsTemp = $weightKilos * 2.20462262;
        document.getElementById("lbs").value = $lbsTemp;
    }
    else {
        document.getElementById("weightout").innerHTML = "Please enter a value";
    }
}

//checks to see what values are selected in a radio group
function radioSelected($rs){
    $rs=document.getElementsByName("sx");
    console.log($rs);
    for(var i=0, length = $rs.length; i<length; i++){
        console.log("length = " + length);
        if($rs[i].checked){
            return $rs[i].value;
        }
    }
}

//calculates lean body mass
function lbmCalc($weightlbs, $bodyFat) {
    $weightlbs = +document.getElementById("lbs").value;
    $bodyFat = +document.getElementById("bf").value; 
    $lbmTemp = ($weightlbs -(($bodyFat / 100)*$weightlbs));
    console.log("lbmTemp:  " + $lbmTemp);
    document.getElementById("lbm").value = $lbmTemp;
}

//this function uses the Mifflin St. Jeor Equation
//For men: BMR = 10 x weight (kg) + 6.25 x height (cm) – 5 x age (years) + 5
//For women: BMR = 10 x weight (kg) + 6.25 x height (cm) – 5 x age (years) – 161

function bmrMSJCalc($gender,$weightKilos,$centField,$age) {
    $gender = document.getElementsByName("sx");
    $weightKilos = +document.getElementById("kg").value;
    $centField = +document.getElementById("cm").value;
    $age = +document.getElementById("ag").value;
    console.log("$age: " + $age);
    console.log("$weightKilos: " + $weightKilos);
    for(var i = 0; i<$gender.length; i++){
        if($gender[i].value == "male" || $gender[i].value == "other"){
            //console.log("this works");
            console.log("$gender[" + i + "] is " + $gender[i].value);
            if($gender[i].value == "male"){
                $bmr = 10*$weightKilos+6.25*$centField-5*$age+5;
                console.log("$bmr: " + $bmr)
            }
            else{
                console.log("$bmr: other");
            }

        }
        else {
            
        };
    };
}

//var sex = document.getElementsByName("sx");

//bmrMSJCalc(sex);
bmrMSJCalc(document.getElementsByName("sx"));

//this function uses the Harris-Benedict Formula
//BMR Formula (Standard English)
    //Women BMR = 655 + (4.35 x weight in pounds) + (4.7 x height in inches) - (4.7 x age in years)
    //Men BMR = 66 + (6.23 x weight in pounds) + (12.7 x height in inches) - (6.8 x age in year)
//BMR Formula (Metric)
    //Women BMR = 655 + (9.6 x weight in kilos) + (1.8 x height in cm) - (4.7 x age in years)
    //Men BMR = 66 + (13.7 x weight in kilos) + (5 x height in cm) - (6.8 x age in years)
function bmrHBCalc() {

}

//this TDEE function uses the Katch-McArdle Formula (BMR based on lean body weight)
//Activity Multiplier
    //Sedentary = BMR X 1.2 (little or no exercise, desk job)
    //Lightly Active = BMR X 1.375 (light exercise/sports 1-3 days/wk)
    //Moderately Active = BMR X 1.55 (moderate exercise/sports 3-5 days/wk)
    //Very Active = BMR X 1.725 (hard exercise/sports 6-7 days/wk)
    //Extremely Active = BMR X 1.9 (hard daily exercise/sports & physical job or 2X day training, etc.)

//BMR (Men and Women) = 370 + (21.6 X lean mass in kg)
"""

