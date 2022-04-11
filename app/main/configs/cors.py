from fastapi.middleware.cors import CORSMiddleware

CORS = {
  'middleware_class': CORSMiddleware,
  'allow_origins': "*",
  'allow_credentials': False,
  'allow_methods': ["*"],
  'allow_headers': ["*"],
}