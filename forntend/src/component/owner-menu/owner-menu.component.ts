import { Component } from '@angular/core';
import { environment } from '../../environments/environment';
import { ActivatedRoute, Router } from '@angular/router';
import { DataService } from '../../service/data.service';
import { AuthService } from '../../service/auth.service';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-owner-menu',
  templateUrl:'./owner-menu.component.html',
  styleUrl: './owner-menu.component.css'
})
export class OwnerMenuComponent {
  dish:any={};
  data: any[] =[];
  is_data = false;
  private logoutUrl=environment.domain+environment.logoutUrl;
  private restaurantUrl=environment.domain+environment.restaurantMenuUrl;

  constructor(
    private route: ActivatedRoute, 
    private dataService: DataService,
    private authService: AuthService, 
    private router:Router) {}

  addDish(dishForm: NgForm){
    if (dishForm.valid){
      this.dataService.postData(this.restaurantUrl,this.dish).subscribe({
      next:(res) =>{
        this.router.navigate(['/owner/home'])
      }
    })
    }
    
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
