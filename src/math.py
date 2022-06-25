from math import gcd
import re
from fastapi import APIRouter,HTTPException
from pydantic import BaseModel

mathapp = APIRouter()

#Todo: mirar que funcioni

    
@mathapp.get("/mcm/{numbers}")
async def get_mcm_list(numbers):
    numbersList = getNumberList(numbers)
    if not numbersList:
         raise HTTPException(status_code=400, detail="Invalid parameter. Empty list")
    mcm = 1
    for x in numbersList:             
        mcm = mcm*x // gcd(mcm,x)
        
    return {"result": mcm}



@mathapp.get("/plus/{number}")
async def get_mcm_list(number :int):
    if not number:
        raise HTTPException(status_code=400, detail="Invalid parameter.")

    return {"result": number + 1}



def mcm(a,b):
    """ Calculate LCM by getting the GCD """
    return (a*b) / gcd(a,b)


def getNumberList(numbers: list[int]):
    """ Formats the incoming list """
    newList = []
    numbers = numbers.replace('[',',')
    numbers = numbers.replace(']',',')
    numbers =numbers.split(',')
    for i in numbers:
        if(i != '' ):
            try:
                if(isinstance(int(i),int)):
                    newList.append(int(i))
            except:
                raise HTTPException(status_code=400, detail="Invalid parameter.")

    return newList