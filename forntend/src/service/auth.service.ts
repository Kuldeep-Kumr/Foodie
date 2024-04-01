import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";

@Injectable({
    providedIn:'root'
})

export class AuthService{
    
    constructor(private http: HttpClient) {}

    post(authUrl:string,user:{}):Observable<{token:string,is_owner:boolean}>{
        return this.http.post<{token:string,is_owner:boolean}>(authUrl,user)
    }
    delete(authUrl:string):Observable<{message:string}>{
        return this.http.delete<{message:string}>(authUrl)
    }
}