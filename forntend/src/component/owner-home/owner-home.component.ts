import { Component } from '@angular/core';
import {  Router } from '@angular/router';
import { DataService } from '../../service/data.service';
import { environment } from '../../environments/environment';
import { AuthService } from '../../service/auth.service';

@Component({
  selector: 'app-owner-home',
  templateUrl:'./owner-home.component.html',
  styleUrl: './owner-home.component.css'
})
export class OwnerHomeComponent {
  logoutUrl=environment.domain+environment.logoutUrl;
  data: any[] =[];
  is_data = false;
  private restaurantUrl=environment.domain+environment.restaurantMenuUrl;
  constructor(
    private dataService: DataService, 
    private router: Router,
    private authService: AuthService
    ) {}

  ngOnInit():void {
    this.dataService.getData(this.restaurantUrl).subscribe({
      next:(res) =>{
        if (res.data.length>0){
          this.is_data=true
        }
        this.data=res.data;
      }
    })
  }
  updateDish(item:any){

      this.dataService.patchData(this.restaurantUrl+item.id+'/',item).subscribe({
      next:(res) =>{
        this.ngOnInit()
      }
    })
  }
  deleteDish(item:any){
    this.dataService.deleteData(this.restaurantUrl+item.id).subscribe({
      next:(res) =>{
        this.ngOnInit()
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
