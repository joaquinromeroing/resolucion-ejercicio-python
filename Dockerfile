FROM python:3.11                             

WORKDIR /app                                                                                                                                            

COPY ejercicioDocker1-2-3/ /app/ejercicioDocker1-2-3/  
COPY ejercicioDocker4-5/ /app/ejercicioDocker4-5/  
COPY ejercicio1/ /app/ejercicio1/          
COPY ejercicio2/ /app/ejercicio2/          

CMD ["bash"]  