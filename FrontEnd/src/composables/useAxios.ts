import axios from 'axios';

function useAxios() {
  const instance = axios.create({
    baseURL: 'http://127.0.0.1:8000/',
    // baseURL: 'http://43.138.126.114:8000/',
  });

  instance.interceptors.request.use(
    (config) => {
      // console.log(config);
      return config;
    },
    (error) => {
      return Promise.reject(error);
    }
  );

  instance.interceptors.response.use(
    (response) => {
      // console.log(response);
      return response;
    },
    (error) => {
      console.log('发生了错误', error);
      return Promise.reject(error);
    }
  );

  return instance;
}

export default useAxios;
