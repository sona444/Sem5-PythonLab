symptoms=['cough','cold','runny nose','body pain','average fever','high fever','Toothache','Stomachache','Headache','Joint Pain','Irritation in Eye','Redness in Eye']
disease=['Viral fever','Covid-19','Dengue','Malaria','Jaundice','Eye flue','Cavity in tooth','Urine Infection','Thyroid','Stomach Infection','Arthritis','Pneumonia','Kidney Stone']
print("Enter symptoms you are facing")
for i in range(len(symptoms)):
    print(i,"  ",symptoms[i],"\n")
x=input()
print("You are suffering from:")
if x==0 or x==1 or x==2 or x==3 or x==4:
    print(disease[0])
elif x==0 and x==5:
    print(disease[1])
