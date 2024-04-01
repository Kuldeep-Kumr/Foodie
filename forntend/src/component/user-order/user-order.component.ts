import { Component } from '@angular/core';
import { environment } from '../../environments/environment';
import { ActivatedRoute, Router } from '@angular/router';
import { DataService } from '../../service/data.service';
import { AuthService } from '../../service/auth.service';

@Component({
  selector: 'app-user-order',
  templateUrl:'./user-order.component.html',
  styleUrl: './user-order.component.css'
})
export class UserOrderComponent {
  payload={
    status:'',
    id:0
  }
  data: any[] =[];
  is_data = false;
  private logoutUrl=environment.domain+environment.logoutUrl;
  private orderUrl=environment.domain+environment.orderUrl;
  constructor(
    private route: ActivatedRoute, 
    private dataService: DataService,
    private authService: AuthService, 
    private router:Router) {}

  ngOnInit():void {
    this.dataService.getData(this.orderUrl).subscribe({
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
