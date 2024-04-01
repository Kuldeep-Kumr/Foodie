import { NgModule } from "@angular/core";
import { BrowserModule } from "@angular/platform-browser";
import { FormsModule } from "@angular/forms";
import { AppRoutingModule} from './app.routing.module';
import { AppComponent} from './app.component';
import { LoginComponent } from "../component/login/login.component";
import { HttpClientModule } from "@angular/common/http";
import { NgFor,NgIf } from "@angular/common";
import { RouterOutlet } from "@angular/router";
import { UserHomeComponent } from "../component/user-home/user-home.component";
import { OwnerHomeComponent } from "../component/owner-home/owner-home.component";
import { UserMenuComponent } from "../component/user-menu/user-menu.component";
import { OwnerMenuComponent } from "../component/owner-menu/owner-menu.component";
import { UserOrderComponent } from "../component/user-order/user-order.component";
import { UserReviewComponent } from "../component/user-review/user-review.component";
import { OwnerOrderComponent } from "../component/owner-order/owner-order.component";
import { RestaurantReviewComponent } from "../component/restaurant-review/restaurant-review.component";
import { ReviewComponent } from "../component/review/review.component";
import { SignupComponent } from "../component/signup/signup.component";

@NgModule({
    declarations:[
        SignupComponent,
        LoginComponent,
        UserHomeComponent,
        OwnerHomeComponent,
        UserMenuComponent,
        OwnerMenuComponent,
        UserOrderComponent,
        UserReviewComponent,
        ReviewComponent,
        OwnerOrderComponent,
        RestaurantReviewComponent
    ],
    imports:[
        AppComponent,
        RouterOutlet,
        BrowserModule,
        AppRoutingModule,
        FormsModule,
        HttpClientModule,
        NgFor,
        NgIf,
    ],
    providers:[],
    bootstrap:[AppComponent]
})

export class AppModule{}