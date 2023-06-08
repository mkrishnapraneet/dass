#  Dockerfile for Node Express Backend

FROM node:17.4.0

# Create App Directory
# RUN mkdir -p /usr/src/app
# WORKDIR /home/mkp/sec_year_sem2/dass/assi_2/app/backend
WORKDIR /usr/app

# Install Dependencies
COPY package*.json ./

RUN npm install --silent

# Copy app source code
COPY . .

# Exports
EXPOSE 4000

CMD ["npm","start"]

# mongodb+srv://user:user@cluster0.zdpnr.mongodb.net/test?retryWrites=true&w=majority
# above is the connection string for mongodb
# 10.1.129.152 is the ip address of the mongodb server for LAN
# 192.168.66.194 is the ip address of the mongodb server for my mobile data