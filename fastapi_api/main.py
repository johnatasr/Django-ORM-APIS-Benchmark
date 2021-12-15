import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from django_main.domain.models import Customer
from fastapi_api.models import customer as cs

app = FastAPI()

model = Customer()
cache = {}
USE_CACHE = False


@app.get("/customer/{customer_id}", response_model=cs.Customer)
async def get_customer(customer_id: int):
    try:
        if USE_CACHE and customer_id in cache:
            return cache.get(customer_id)

        db_customer = await model.async_customer_actions.get_last_customer()
        res_customer = cs.Customer(**db_customer.to_dict())
        cache[customer_id] = res_customer
        return res_customer
    except Exception as e:
        print(e)
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"error": "Customer not Found!"})


@app.post("/customer", response_model=cs.Customer)
async def customer(cust: cs.Customer):
    print(f"got new customer for creation: {cust}")
    try:
        db_customer = await model.async_customer_actions.create_customer(name=cust.name, domain=cust.domain, is_active=True)
        res_customer = cs.Customer(**db_customer.to_dict())
        return res_customer
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error": e})


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5002, loop='uvloop', workers=1)
