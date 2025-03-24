
import api from "./api";

  export async function  getsellorders(uid){
         return api.get(`sellorder/${uid}/`)
    }


  export async function  getbuyorders(uid){
        return api.get(`buyorder/${uid}/`)
    }

  export async function getfeedback(uid){
      return api.get(`feedback/${uid}/`)
  }