import { Component } from '@angular/core';
import { environment } from '../../environments/environment';
import { ActivatedRoute, Router } from '@angular/router';
import { DataService } from '../../service/data.service';
import { AuthService } from '../../service/auth.service';

@Component({
  selector: 'app-owner-order',
  templateUrl:'./owner-order.component.html',
  styleUrl: './owner-order.component.css'
})
export class OwnerOrderComponent {
  payload={
    status:'',
    id:0
  }
  data: any[] =[];
  is_data = false;
  private logoutUrl=environment.domain+environment.logoutUrl;
  private restaurantOrderUrl=environment.domain+environment.restaurantOrderUrl;
  constructor(
    private route: ActivatedRoute, 
    private dataService: DataService,
    private authService: AuthService, 
    private router:Router) {}

  ngOnInit():void {
    this.dataService.getData(this.restaurantOrderUrl).subscribe({
      next:(res) =>{
        if (res.data.length>0){
          this.is_data=true
        }
        this.data=res.data;
      }
    })
  }

  update(data:any){
    this.payload.status=data.status
    this.payload.id=data.id
    this.dataService.patchData(this.restaurantOrderUrl+this.payload.id+'/',this.payload).subscribe(()=>{ 
      this.ngOnInit()
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
