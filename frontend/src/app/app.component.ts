import {Component, ElementRef, OnInit} from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {TestServiceService} from './test-service.service';
import { CommonModule } from '@angular/common';
import { BrowserModule } from '@angular/platform-browser';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, CommonModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
  providers: [TestServiceService]
})
export class AppComponent implements OnInit{
  dataClass: any;
  studentList: any;
  namesList : any;
  attendanceList: any = [];
  commentList: any = [];
  behaviourType: any = [];
  report: any = [];
  constructor(private testService: TestServiceService) {

  }
  ngOnInit(): void {
    this.testService.fetchNames().subscribe(data => {
        this.testService.setNames(data);
        this.namesList = this.testService.getNames();
    })
  }

  addElement(x:any){
    this.attendanceList.push(x);
  }

  setCommentList(x:any){
    this.commentList.push(x);
  }

   setBehaviourType(x:any){
    this.behaviourType.push(x);
  }

  setAttendanceList(x:any){
    this.attendanceList = x;
  }

  sendBehaviour(){
    this.testService.addBehaviour(this.behaviourType, this.commentList).subscribe(data => {
      console.log("behaviour added");
    })
  }

  sendAttendance(){
    this.testService.sendAttendance(this.attendanceList).subscribe(data => {
      this.setAttendanceList([]);
      this.sendBehaviour();
    });
  }

  getReport(){
    this.testService.fetchReport().subscribe(data => {
       this.testService.setReport(data);
       this.report = this.testService.getReport();
    })
  }

  setClass(x: any){
    this.testService.setClass(x);
      this.testService.fetchClassData().subscribe(data => {
        this.testService.setData(data);
        this.dataClass = this.testService.getData();
        this.studentList = this.testService.getStudentData();
      }
    )
  }

  setStudent(x:any){
    this.testService.setStudent(x);
  }
  title = 'frontend';


}
