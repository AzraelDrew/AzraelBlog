cd azraelhtml; 
npm i;
cd ..;
cd AzraelSite;
mkdir upload ;
python3 manage.py makemigrations &  python3 manage.py migrate;

