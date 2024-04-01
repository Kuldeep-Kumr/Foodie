import { Component } from '@angular/core';
import { environment } from '../../environments/environment';
import { ActivatedRoute, Router } from '@angular/router';
import { DataService } from '../../service/data.service';
import { AuthService } from '../../service/auth.service';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-review',
  templateUrl: './review.component.html',
  styleUrl: './review.component.css'
})
export class ReviewComponent {
  dish:any={};
  data: any[] =[];
  is_data = false;
  private restaurantId='';
  private logoutUrl=environment.domain+environment.logoutUrl;
  private reviewUrl=environment.domain+environment.reviewUrl;
  constructor(
    private route: ActivatedRoute, 
    private dataService: DataService,
    private authService: AuthService, 
    private router:Router) {}

  addReview(dishForm:NgForm){
    this.dish.menu=this.route.snapshot.params['id'];
    if (dishForm.valid){
      this.dataService.postData(this.reviewUrl,this.dish).subscribe({
      next:(res) =>{
        this.router.navigate(['/user/review'])
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
