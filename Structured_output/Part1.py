from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatOpenAI()

# schema
class Review(TypedDict):
   summary : str 
   sentiment : str

structured_model = model.with_structured_output(Review)
result = structured_model.invoke(""" I recently bought the XYZ wireless earbuds after reading several positive reviews. The sound quality is excellent, and the noise cancellation works much better than I expected. The battery easily lasts an entire day, which is perfect for my work schedule. However, the earbuds become slightly uncomfortable after wearing them for more than three hours, and the mobile app occasionally disconnects from the device. Despite these minor issues, I believe the product offers great value for money and I would definitely recommend it to others.
""")
print(result)
print(result["summary"])
print(result["sentiment"])

