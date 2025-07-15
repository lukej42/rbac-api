import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    user = req.headers.get("X-MS-CLIENT-PRINCIPAL")
    if not user:
        return func.HttpResponse("Unauthorized", status_code=401)
    
    # Optionally decode and inspect the claims here
    return func.HttpResponse("Hello from Python Function with RBAC!", status_code=200)
