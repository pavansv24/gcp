import google.generativeai as genai
import PIL.Image

API_KEY = 'AIzaSyA0wLuydwFA1cvzbQ-S5NLuLRKRYpivAq0'

genai.configure(api_key=API_KEY)



img = PIL.Image.open('../ppeV2/train/images/20240216_160223_mp4-0454_jpg.rf.9ddb2e9e524a56dfc4c6d64ec907a3af.jpg')
#img

model = genai.GenerativeModel('gemini-pro-vision')
response = model.generate_content(img)

text="one persoan should be ware ppe_kit .First you focus on the persoan and Can you detect if the persoan is wearing all the seafty kit or not?in reponse don't describe only give the kit name that not worned among from which i gave you . catagorize into available & non available in one line only"
response = model.generate_content([text, img], stream=True)
response.resolve()

str=response.text
split_variable = str.split("\n")
print(split_variable)


