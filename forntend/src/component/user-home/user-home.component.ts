import { Component } from '@angular/core';
import { DataService } from '../../service/data.service';
import { environment } from '../../environments/environment';
import { AuthService } from '../../service/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-user-home',
  templateUrl:'./user-home.component.html',
  styleUrl: './user-home.component.css'
})
export class UserHomeComponent {
  payload={
    token:''
  }
  data: any[]=[];
  is_data = false
  private logoutUrl=environment.domain+environment.logoutUrl;
  
  constructor(private dataService: DataService,private authService:AuthService,private router : Router) {}

  ngOnInit(): void {
    this.dataService.getData(environment.domain+environment.restaurantUrl).subscribe({
      next:(res) =>{
        if (res.data.length>0){
          this.is_data=true
        }
        this.data=res.data;
      }
    })
  }
  logout(){
    this.logoutUrl+=sessionStorage.getItem('token')
    this.authService.delete(this.logoutUrl).subscribe({
      next:(res) =>{
        this.router.navigate(['/'])
      }
    })
  }
}
