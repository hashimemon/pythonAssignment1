cities={
    "Karachi":{
        "country":"Pakistan",
        "population":15741000,
        "fact":"""Karachi is vital to Pakistan's economy, contributing 42 per cent of GDP,
        70 per cent of income tax revenue and 62 per cent of sales tax revenue"""
    },
    "Lahore":{
        "country":"Pakistan",
        "population":12188000,
        "fact":"""Lahore is the capital city of the Pakistani province of Punjab.
        It is the second largest and most populous city in Pakistan"""
    },
    "Islamabad":{
        "country":"Pakistan",
        "population":1095064,
        "fact":"""Islamabad is the capital of the top adventurous place Pakistan.This city
        is famous due to the many parks, forests, greenery, breathtaking sites, safety,
        high living standard, world fourth largest mosque and the Margalla Hills National park."""
    }
}
for citykey,cityinfo in cities.items():
    print("\n"+citykey+"\n")
    for city in cityinfo:
        print(city,":",str(cityinfo[city]))
