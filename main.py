from fastapi import FastAPI
import random
from pydantic import BaseModel
import json


app = FastAPI()

class Age(BaseModel):
    age : int


# Sample values for each field
class Sib():
    names = ["shravya", "Sampada", "Divyanka", "Amanika", "Monalisa", "Kavya", "Rashmi", "Mamta"]
    names_ml = ["ശ്രവ്യ", "സമ്പത്ത്", "ദിവ്യങ്ക", "അമാനിക", "മോണാലിസ", "കാവ്യ", "രശ്മി", "രശ്മി"]
    branches = ["DIAMOND POINT-SECUNDERABAD", "DWARKA-NEW DELHI", "FORT BRANCH-MUMBAI", "G T,CHENNAI", "HATIBAGAN,KOLKATA", "VIMAN NAGAR,PUNE", "BANGALORE BRIGADE ROAD", "BANGALORE DEVANAHALLI"]
    branches_ml = ["ഡയമണ്ട് പോയിൻറ് -സികന്ദരാബാദ്‌", "ദ്വാരക -ന്യൂ ഡൽഹി", "ഫോർട്ട്‌ ബ്രാഞ്ച് -മുംബൈ", "ജി ടി ,ചെന്നൈ", "ഹതിബാഗൻ ,കൊൽക്കത്ത", "വിമൺ നഗർ, പുണെ", "ബാംഗ്ലൂർ  ബ്രിഗേഡ് റോഡ്‌", "ബാംഗ്ലൂർ ദേവനഹള്ളി"]
    phone_numbers = ["+918104035237", "+919518969574", "+919547531359","+919437986364"]
    salutations = ["Sir","Sir","Ma'am","Ma'am","Ma'am","Sir","Sir","Ma'am"]
    salutations_ml = ["സാർ","സാർ","മാഡം","മാഡം","മാഡം","സാർ","സാർ","മാഡം"]


class Tli():
    insurance_providers =["ICICI Pru","HDFC Life","PNB Metlife","TATA AIA","Bajaj Allianz Life","Max Life","Canara HSBC","Kotak","Edelweiss Tokio","Aegon Life","Aditya Birla ABSLI","SBI","No Plans Available"]
    plan_names=["iProtect Smart","Click 2 Protect Super","Mera Term Plan Plus","Sampoorna Raksha Supreme","eTouch Plan","Smart Secure Plus Plan","iSelect Smart 360 Term Plan","e-Term Plan","Zindagi Protect Plan","iTerm Prime","DigiShield Plan","eShield Next","No Plans Available"]
    claimsettlements=["97.8","99.4","99.1","99","99","99.5","99","98.5","99.2","99.4","98.1","95","No Plans Available"] 
    entryages=["18 to 65 years","18 to 65 years","18 to 65 years","18 to 60 years","18 to 65 years","18 to 65 years","18 to 65 years","18 to 65 years","18 to 65 years","18 to 60 years","18 to 45 years","18 to 45 years","Below 18"]
    policyterms=["Up to 85 years","Up to 85 years","Up to 80 years","Up to 85 years","Up to 85 years","Up to 85 years","Up to 85 years","Up to 85 years","Up to 85 years","Up to 85 years","Up to 85 years","Up to 85 years","No Plans Available"]
    monthlypremiums=["Rs. 2,095","Rs. 1,837","Rs. 1,840","Rs. 1,549","Rs. 1,391","Rs. 1,693","Rs. 1,482","Rs. 1,672","Rs. 1,585","Rs. 2,083","Rs. 1,081","Rs. 2,197","No Plans Available"] 
    annualpremiums =["Rs. 24,525","Rs. 20,997","Rs. 20,768","Rs. 17,543","Rs. 15,899","Rs. 19,235","Rs. 16,469","Rs. 18,998","Rs. 18,002","Rs. 23,946","Rs. 12,010","Rs. 25,826","No Plans Available"]


class Consent():
    use_cases = ["Credit Check for Loan Application","Credit Check for Loan Application","Employment Verification for Mortgage Approval","Employment Verification for Mortgage Approval","Financial Transaction Analysis for Investment Consultation","Financial Transaction Analysis for Investment Consultation"]
    use_cases_hi = ["ऋण आवेदन के लिए क्रेडिट जाँच","ऋण आवेदन के लिए क्रेडिट जाँच","ऋण जाँच के लिए रोजगार स्वीकृति","ऋण जाँच के लिए रोजगार स्वीकृति","निवेश परामर्श के लिए फाइनेंसियल लेनदेन विश्लेषण","निवेश परामर्श के लिए फाइनेंसियल लेनदेन विश्लेषण"]
    use_cases_bn = ["ঋণের আবেদনের জন্য ক্রেডিট চেক,","ঋণের আবেদনের জন্য ক্রেডিট চেক,","বন্ধকী অনুমোদনের জন্য কর্মসংস্থান যাচাইকরণ,","বন্ধকী অনুমোদনের জন্য কর্মসংস্থান যাচাইকরণ,","বিনিয়োগ পরামর্শের জন্য আর্থিক লেনদেন বিশ্লেষণ","বিনিয়োগ পরামর্শের জন্য আর্থিক লেনদেন বিশ্লেষণ"]
    duration = ["6 months","1 year","6 months","1 year","6 months","1 year"]
    duration_hi = ["6 महीने","1 वर्ष","6 महीने","1 वर्ष","6 महीने","1 वर्ष"]
    duration_bn = ["ছয় মাস","এক বছর","ছয় মাস","এক বছর","ছয় মাস","এক বছর"]


class CarDekho():
    user=["Aarya","Divya","Jaya","Lavanya","Kimaya","Saumya","Suman","Zoya","Amulya"]
    car=["Mercedes-Benz GLE Coupe","Audi Q8", "Porsche Cayenne Coupe", "Range Rover Velar","Lexus RX","Infiniti QX70","Acura MDX","Volvo XC90","BMW X6"]
    user_hi=["आर्या","दिव्या","जया","लावण्या","किमाया","सौम्या","सुमन","जोया","अमूल्य"]
    car_hi=["मर्सिडीज-बेंज जीएलई कूप","ऑडी क्यू एट","पोर्श केयेन कूप","रेंज रोवर वेलार","लेक्सस आरएक्स","इनफिनिटी क्यू एक्स सेवेंटी","एक्यूरा एमडीएक्स","वोल्वो एक्स सी नाइनटी","बीएमडब्ल्यू एक्स सिक्स"]
    phone_number=["9876543210","9897563412","9909876789","9984531342","8765678345","6544678654","7678987679","8907896785","7658769870"]


class IDBI_FD():
    all_details = [
    {
        "account_holder":"Alia Sharma",
        "account_holder_hi":"आलिया शर्मा",
        "account_numbers": ["1926", "2483", "3259"],
        "pan_number": "A B C D E 2 2 2 2 B",
        "nominee_name": "Jay",
        "nominee_name_hi":"जय",
        "nominee_relation": "Your son",
        "nominee_relation_hi": "आपका बेटा"
    },
    {
        "account_holder":"Maya Jha ",
        "account_holder_hi":"माया झा",
        "account_numbers": ["4831", "5823", "6119"],
        "pan_number": "G B F D E 2 2 2 2 B",
        "nominee_name": "Rahul",
        "nominee_name_hi":"राहुल",
        "nominee_relation": "Your husband",
        "nominee_relation_hi":"आपके पति"
    },
    {
        "account_holder":"Anisha Patel",
        "account_holder_hi":"अनिशा पटेल",
        "account_numbers": ["7174", "8759", "9142"],
        "pan_number": "H I F C K 2 2 2 2 B",
        "nominee_name": "Anjali",
        "nominee_name_hi": "अंजलि",
        "nominee_relation": "Your daughter",
        "nominee_relation_hi":"आपकी बेटी",
    },
        {
        "account_holder":"Gauri Kulkarni",
        "account_holder_hi":"गौरी कुलकर्णी",
        "account_numbers": ["7174", "8759", "9142"],
        "pan_number": "M G Y O E 0 5 3 2 K",
        "nominee_name": "Lila",
        "nominee_name_hi": "लीला",
        "nominee_relation": "Your mother",
        "nominee_relation_hi":"आपकी माँ",
    },
        {
        "account_holder":"Rashmi Kumari",
        "account_holder_hi":"रश्मी कुमारी",
        "account_numbers": ["7174", "8759", "9142"],
        "pan_number": "T Y V R T 7 8 4 5 M",
        "nominee_name": "Lokesh",
        "nominee_name_hi": "लोकेश",
        "nominee_relation": "Your father",
        "nominee_relation_hi":"आपके पिता",
    },
        {
        "account_holder":"Meenakshi Matthew",
        "account_holder_hi":"मीनाक्षी मैथ्यू",
        "account_numbers": ["7174", "8759", "9142"],
        "pan_number": "M G U O S 0 6 8 2 K",
        "nominee_name": "Anamika",
        "nominee_name_hi": "अनामिका",
        "nominee_relation": "Your daughter",
        "nominee_relation_hi":"आपकी बेटी",
    },
    # Add more details sets as needed
    ]

# Add more sample values for other fields as needed

@app.get('/')
def start():
    message = "App is running!"
    return message

@app.get("/sib_data")
def get_random_values():
    # Selecting random values for each field
    index = 0
    index = random.randint(0,7)
    name = Sib.names[index]
    name_ml = Sib.names_ml[index] 
    branch = Sib.branches[index]
    branch_ml = Sib.branches_ml[index]
    phone_number = random.choice(Sib.phone_numbers)
    salutation = Sib.salutations[index]
    salutation_ml = Sib.salutations_ml[index]
    # Add more random choices for other fields as needed

    # Creating a dictionary to hold the random values
    random_data = {
        "name": name,
        "name_ml": name_ml,
        "branch": branch,
        "branch_ml": branch_ml,
        "phone number" : phone_number,
        "salutation" : salutation,
        "salutation_ml" : salutation_ml
        # Add more fields here with their respective random values
    }
    return random_data


@app.post('/tli_data/')
async def tli_data(age_num :Age):
    data = []
    idx = []
    age = age_num.age 
    if age < 18:
        idx = [12]
    elif age < 46:
        idx = [0,1,2,3,4,5,6,7,8,9,10,11]
    elif age < 61:
        idx = [0,1,2,3,4,5,6,7,8,9]
    elif age < 65:
        idx = [0,1,2,4,5,6,7,8]

    for i in range(len(idx)):
        item = {
            "insurance_provider": Tli.insurance_providers[idx[i]],
            "plan_name": Tli.plan_names[idx[i]],
            "claimsettlement": Tli.claimsettlements[idx[i]],
            "entryage": Tli.entryages[idx[i]],
            "policyterm": Tli.policyterms[idx[i]],
            "monthlypremium": Tli.monthlypremiums[idx[i]],
            "annualpremium": Tli.annualpremiums[idx[i]],
        }
        data.append(item)
    
    print(data)
    json_string = json.dumps(data, ensure_ascii=False)
    json_string= json.loads(json_string)
    jsona = {"data":json_string}

    return jsona



@app.get('/consent_data')
def consent_data():

    index = 0
    index = random.randint(0,5)
    use_case = Consent.use_cases[index]
    use_case_hi = Consent.use_cases_hi[index]
    use_case_bn = Consent.use_cases_bn[index]

    duration = Consent.duration[index]
    duration_hi = Consent.duration_hi[index]
    duration_bn = Consent.duration_bn[index]



    data = {
        "use_case":use_case,
        "use_case_hi":use_case_hi,
        "use_case_bn":use_case_bn,
        "duration":duration,
        "duration_hi":duration_hi,
        "duration_bn":duration_bn,

    }

    return data

@app.get('/cardekho_data')
def cardekho_data():

    index = 0
    index = random.randint(0,3)
    user = CarDekho.user[index]
    user_hi = CarDekho.user_hi[index]
    car = CarDekho.car[index]

    car_hi = CarDekho.car_hi[index]
    number = CarDekho.phone_number[index]




    data = {
        "user":user,
        "user_hi":user_hi,
        "car":car,
        "car_hi":car_hi,
        "phone_number":number,

    }

    return data

@app.get("/idbi_fd")
def get_details():
    # Randomly select one set of details
    selected_details = random.choice(IDBI_FD.all_details)
    return selected_details