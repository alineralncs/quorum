# Quorum 

Para rodar este projeto localmente em sua máquina, siga as etapas abaixo


## Running Locally

Clone the project

```bash
  git clone https://github.com/alineralncs/quorum.git
```

Navigate to the project directory

```bash
  cd quorum
```

Install Anaconda for the virtual environment

``` bash 
[How to Install Anaconda on Windows] https://hub.asimov.academy/blog/como-instalar-anaconda-no-windows/
```

Create and activate the environment

```bash
  conda create --name nome_ambiente python
  conda activate nome_ambiente
```

Install dependencies

```bash
   pip install -r requirements.txt
```

Start the server

```bash
  python manage.py runserver
```

## Visit the site 

http://localhost:8000/


### By visiting the site you can see the list of legislators and bills available, and to view the details of each one, simply select one.