import { Component, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {TestServiceService} from './test-service.service';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
  providers: [TestServiceService]
})
export class AppComponent implements OnInit{
  private totalAngularPackages: any = [];
  constructor(private testService: TestServiceService) {

  }
  ngOnInit(): void {
    this.testService.fetchData().subscribe(data => {
        this.totalAngularPackages  = data;
        console.log(data);
      }
    )
  }

  getTotalAngularPackages(){
    return this.totalAngularPackages;
  }
  title = 'frontend';


}
