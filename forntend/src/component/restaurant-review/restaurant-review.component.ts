import { Component } from '@angular/core';
import { environment } from '../../environments/environment';
import { ActivatedRoute, Router } from '@angular/router';
import { DataService } from '../../service/data.service';
import { AuthService } from '../../service/auth.service';

@Component({
  selector: 'app-restaurant-review',
  templateUrl:'./restaurant-review.component.html',
  styleUrl: './restaurant-review.component.css'
})
export class RestaurantReviewComponent {
  data: any[] =[];
  is_data = false;
  private logoutUrl=environment.domain+environment.logoutUrl;
  private reviewUrl=environment.domain+environment.reviewUrl;
  private menuId='';
  constructor(
    private route: ActivatedRoute, 
    private dataService: DataService,
    private authService: AuthService, 
    private router:Router) {}

  ngOnInit():void {
    this.menuId = this.route.snapshot.params['id'];
    this.reviewUrl += this.menuId
    this.dataService.getData(this.reviewUrl).subscribe({
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
