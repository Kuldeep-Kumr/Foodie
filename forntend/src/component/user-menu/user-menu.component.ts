import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { DataService } from '../../service/data.service';
import { environment } from '../../environments/environment';
import { AuthService } from '../../service/auth.service';

@Component({
  selector: 'app-user-menu',
  templateUrl: './user-menu.component.html',
  styleUrl: './user-menu.component.css'
})
export class UserMenuComponent {
  payload={
    menu:0,
    quantity:1,
    token:'',
  }
  data: any[] =[];
  is_data = false;
  private restaurantId='';
  private logoutUrl=environment.domain+environment.logoutUrl;
  private restaurantUrl=environment.domain+environment.restaurantUrl;
  constructor(
    private route: ActivatedRoute, 
    private dataService: DataService,
    private authService: AuthService, 
    private router:Router) {}

  ngOnInit():void {
    this.restaurantId = this.route.snapshot.params['id'];
    this.restaurantUrl += this.restaurantId
    this.dataService.getData(this.restaurantUrl).subscribe({
      next:(res) =>{
        if (res.data.length>0){
          this.is_data=true
        }
        this.data=res.data;
      }
    })
  }

  placeOrder(data:any){
    this.payload.menu=data.id
    this.payload.quantity=data.quantity
    this.dataService.postData(environment.domain+environment.orderUrl,this.payload).subscribe(()=>{ 
      this.router.navigate(['/user/order'])
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
