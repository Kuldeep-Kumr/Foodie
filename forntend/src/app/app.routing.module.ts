import { RouterModule, Routes} from '@angular/router';
import { LoginComponent } from '../component/login/login.component';
import { NgModule } from '@angular/core';
import { UserHomeComponent } from '../component/user-home/user-home.component';
import { OwnerHomeComponent } from '../component/owner-home/owner-home.component';
import { UserMenuComponent } from '../component/user-menu/user-menu.component';
import { OwnerMenuComponent } from '../component/owner-menu/owner-menu.component';
import { UserOrderComponent } from '../component/user-order/user-order.component';
import { UserReviewComponent } from '../component/user-review/user-review.component';
import { OwnerOrderComponent } from '../component/owner-order/owner-order.component';
import { RestaurantReviewComponent } from '../component/restaurant-review/restaurant-review.component';
import { ReviewComponent } from '../component/review/review.component';
import { SignupComponent } from '../component/signup/signup.component';

export const routes: Routes=[
    {path:'signup',component:SignupComponent,title:"Signup"},
    {path:'',component:LoginComponent,title:'Login'},
    {path:'user/home',component:UserHomeComponent,title:'Foodie'},
    {path:'owner/home',component:OwnerHomeComponent,title:'Foodie'},
    {path:'user/menu/:id',component:UserMenuComponent,title:'Menu'},
    {path:'owner/menu',component:OwnerMenuComponent,title:'Add Menu'},
    {path:'owner/review/:id',component:RestaurantReviewComponent,title:'Review'},
    {path:'user/order',component:UserOrderComponent,title:'Order'},
    {path:'user/review',component:UserReviewComponent,title:"Review"},
    {path:'user/review/:id',component:ReviewComponent,title:"Review"},
    {path:'owner/order',component:OwnerOrderComponent,title:"Restaurant Order"}
];

@NgModule({
    imports:[RouterModule.forRoot(routes)],
    exports:[RouterModule]
})

export class AppRoutingModule{}