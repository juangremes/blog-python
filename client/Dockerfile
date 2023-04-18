FROM node:16.17.0
 
# These env vars are needed so that CRA can execute in a docker container
ENV CI=true
ENV WDS_SOCKET_PORT=0
# Added by me
# ENV NODE_OPTIONS=--openssl-legacy-provider  

 
WORKDIR /app
COPY public ./public
COPY src ./src
COPY package.json ./

RUN npm install
 
CMD ["npm", "start"]