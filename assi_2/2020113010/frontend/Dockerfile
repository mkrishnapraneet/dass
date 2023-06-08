# Dockerfile for React client

# Build react client
FROM node:17.4.0

# Working directory be app
# WORKDIR /home/mkp/sec_year_sem2/dass/assi_2/app/frontend
WORKDIR /usr/app

COPY package*.json ./

###  Installing dependencies

RUN npm install 

# copy local files to app folder
COPY . .

EXPOSE 3000

CMD ["npm","start"]