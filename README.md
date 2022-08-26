# ecom_api
# Clone the repository
git clone https://github.com/Neha5660/ecom_api.git
# Activate virtual environment
 venv/Scripts/Activate
# Otherwise install library using the requirement file
pip install -r requirement.txt
# Run the server
 #  Move to file
  cd ecom_api/ecomapi/
  python manage.py runserver
  
# urls
 # Show the all categories from database  and you can also add the new category by using Post
  http://127.0.0.1:8000
 # Show the one categories from database  and you can also update and delete category by using Put,Delete
  http://127.0.0.1:8000/1
  # Show the all cloth from database  and you can also add the new cloth by using Post
  http://127.0.0.1:8000/cloth
 # Show the one cloth from database  and you can also update and delete cloth by using Put,Delete
  http://127.0.0.1:8000/cloth/1
  # Show the all product from database  and you can also add the new product by using Post
  http://127.0.0.1:8000/product
 # Show the one product from database  and you can also update and delete product by using Put,Delete
  http://127.0.0.1:8000/product/1
  
 # Docker
 # Add docker file that have configuration to containerised the application
    # Dockerfile
    docker-compose build
 # Add docker compose file that have application information what is the ip and port
    # docker-compose.yml
    docker-compose up
