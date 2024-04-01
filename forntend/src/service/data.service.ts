import { Injectable } from "@angular/core";
import { HttpClient,HttpHeaders } from "@angular/common/http";

@Injectable({
    providedIn:'root'
})
export class DataService{
    constructor(private http:HttpClient) {}
    private token = sessionStorage.getItem('token')
    private headers = new HttpHeaders({
            'Authorization': 'Bearer '+this.token
        });
    getData(url:string){
        return this.http.get<{message:string,data:[]}>(url,{headers:this.headers});
    }
    postData(url:string,payload:{}){
        return this.http.post<{message:string,data:[]}>(url,payload,{headers:this.headers});
    }
    patchData(url:string,payload:{}){
        return this.http.patch<{message:string,data:[]}>(url,payload,{headers:this.headers});
    }
    deleteData(url:string){
        return this.http.delete<{message:string}>(url,{headers:this.headers});
    }
}