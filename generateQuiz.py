
from langchain.prompts import PromptTemplate
from langchain import LLMChain, PromptTemplate
from langchain.chat_models import ChatOpenAI




OPENAI_API_KEY = "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"
model_name='gpt-4'

# model_name='gpt-3.5-turbo'
llm = ChatOpenAI(model_name=model_name,temperature=0,openai_api_key=OPENAI_API_KEY)

def generateMCQS(text):
  prompt_templateMCQS = """You are a university professor making a quiz with your knowledge for your student which test conceptual and critical thinking skills
    of a student. I'll provide you with some information and
  ask you a MCQ question based on that source 
  and the correct answer.
  Your job is to explain why the correct option
  is correct and why other otions are incorrect(provide this information on the last of the response) on the source information I provide you also mention correct option at the end:

  {context}

  Question: {question}

  please generate the response in following format:

  Question Statement
    a) Option A
    b) Option B
    c) Option C
    d) Option D

  Option A: Explanation of option A

  Option B: Explanation of option B

  Option C: Explanation of option C

  Option D: Explanation of option D

  Correct Option: [Correct option as, "A", "B", "C", or "D"]

  ####
  Note: Don't give the options that are partially correct.

  I want to ensure that the format remains the same for each of the questions, options, correct answers, explanations, and ####. Thank you.
  The questions should be open-ended, add examples if possible, focus on why more and at the high difficulty level for a university student.  

  """
  PROMPTMCQS = PromptTemplate(
      template=prompt_templateMCQS, input_variables=["context", "question"]
  )

  chainMCQS = LLMChain(llm=llm , prompt=PROMPTMCQS)
  questionMCQS = "Please generate in-depth multiple-choice questions, each question should have four options. The questions should be about the main concepts, insights, and implications. Also mention in the explaination why the oprion is correct and why its not correct"
  ouptutMCQS = chainMCQS.predict(context=text, question=questionMCQS)
  return ouptutMCQS


def generateFAQs(text):
  prompt_templateFAQS = """You are a university professor making a quiz with your knowledge for your student which test conceptual and critical thinking skills
    of a student. I'll provide you with some information and ask you to generate open ended questions based on that source and the answer based on source.
    Question should be in the form that it requiress the Answer in two or three bullet points.

  Your job is to explain why the answer is correct(provide this information on the last of the response) based on the source information I provide you:

  {context}

  Question: {question}

  please generate the response in following format:

  1. Question?
  Answer: [Bullet point one] # [Bullet point two] # [Bullet point three]

  Explanation: [Explanation why the bullet one is correct] # [Explanation why the bullet two is correct] # [Explanation why the bullet three is correct]

  ####

  I want to ensure that the format remains the same for each of the questions, answers, explanations, and ####. Thank you.
  The questions should be open-ended, add examples if possible, focus on why more and at the high difficulty level for a university student.  

  """
  PROMPTFAQS = PromptTemplate(
      template=prompt_templateFAQS, input_variables=["context", "question"]
  )
  chainFAQS = LLMChain(llm=llm , prompt=PROMPTFAQS)
  questionFAQS = "Please generate in-depth FAQ questions. The questions should be about the main concepts, insights, and implications."
  ouptutFAQS = chainFAQS.predict(context=text, question=questionFAQS)
  return ouptutFAQS



def generate(chunck):
    MCQ = generateMCQS(chunck)
    listFinal = []
    listQuestions = MCQ.split("####")
    for x in listQuestions:
        questionDic = {}
        extracted = x.strip()
        extracted = extracted.split("\n")
        cleanExtracted = []
        for y in extracted:
            if y != '':
                cleanExtracted.append(y.strip())
        try:
            questionDic["question"] = cleanExtracted[0].split(":")[-1].strip()
            questionDic["type"] = "MCQS"
            questionDic["Choices"] = [cleanExtracted[1].split(")")[-1].strip(),cleanExtracted[2].split(")")[-1].strip(),cleanExtracted[3].split(")")[-1].strip(),cleanExtracted[4].split(")")[-1].strip()]
            questionDic["choicesDescriptions"] = [cleanExtracted[5].replace("[", "").replace("]", "").split(":")[-1].strip(),cleanExtracted[6].replace("[", "").replace("]", "").split(":")[-1].strip(),cleanExtracted[7].replace("[", "").replace("]", "").split(":")[-1].strip(),cleanExtracted[8].replace("[", "").replace("]", "").split(":")[-1].strip()]
            questionDic["correctAnswer"] = cleanExtracted[9][-1]
            listFinal.append(questionDic)
        except:
            pass
    return listFinal

