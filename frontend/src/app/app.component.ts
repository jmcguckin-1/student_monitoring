import {Component, ElementRef, OnInit} from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {TestServiceService} from './test-service.service';
import { CommonModule } from '@angular/common';
import { BrowserModule } from '@angular/platform-browser';
import { NzProgressModule } from 'ng-zorro-antd/progress';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, CommonModule, NzProgressModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
  providers: [TestServiceService, NzProgressModule],
  styles: [
    `
      nz-progress {
        margin-right: 8px;
        margin-bottom: 8px;
        display: inline-block;

      }
    `
  ]
})
export class AppComponent implements OnInit{
  dataClass: any;
  studentList: any;
  namesList : any;
  attendanceList : any = {};
  commentList: any = {};
  behaviourType: any = {};
  studentLength: any;
  report: any = [];
  behaviourReport: any = [];
  studentReportName: any;
  gradesList: any = [];
  overallAttendance: any;
  currentGrade: number = 0;
  currentAssignmentComment: any;
  allAssignments: any = [];
  currentAssignment: any;
  hasSubmitted : any;
  constructor(private testService: TestServiceService) {

  }
  ngOnInit(): void {
    this.testService.fetchNames().subscribe(data => {
        this.testService.setNames(data);
        this.namesList = this.testService.getNames();
    })

  }

  createDefaults(data:any){
    let aList: any = {};
    let cList: any = {};
    let bType: any = {};
    for (let i=0; i<data.length; i++){
      aList[data[i]] = "P";
      cList[data[i]] = "";
      bType[data[i]] = "M";
    }
    this.setAttendanceList(aList);
    this.setBehaviourList(bType);
    this.setCommentList(cList);
  }

  addElement(x:any, name:any){
    if (Object.keys(this.attendanceList).length <= this.studentLength){
        this.attendanceList[name] = x;
    }
  }

  setComment(x:any){
    this.testService.setComment(x);
  }

  setCG(x:any){
    this.currentGrade = x;
  }
  getFullReport(){
    this.testService.getFullReport().subscribe(data => {
          this.testService.setFullReport(data);
          this.gradesList = this.testService.getGradesCommentList();
          this.studentReportName = this.testService.getStudentReportName();
          this.overallAttendance = this.testService.getOverallAttendance();
    })
  }

  addComment(){
    this.testService.addComment().subscribe(data => {
    })
  }

  getCurrentStudent(){
    return this.testService.getCurrentStudent();
  }

  setAssignmentComment(x:any){
    this.currentAssignmentComment = x;
    this.testService.setAssignment(x);
  }

  markAssignment(){
    this.testService.markAssignment(this.currentGrade, this.currentAssignmentComment, this.currentAssignment).subscribe(data => {

    })
  }

  setAssignments(x:any){
    this.allAssignments = x[0];
    this.setAssignment(this.allAssignments[0]);
  }

  setAssignment(x: any){
    this.currentAssignment = x;
    this.testService.setAssignment(x);
    this.testService.hasStudentSubmitted().subscribe(data => {
     this.hasSubmitted = data;

     if (this.hasSubmitted['late']){
       this.testService.updateBehaviour("C", "Assignment Handed in Late").subscribe(data => {

       })
     }

     if (!this.hasSubmitted['submitted']){
       this.testService.updateBehaviour("SV", "Assignment Not handed in").subscribe(data => {

       })
     }
    })
  }

  getAssignmentNames(){
    this.testService.getAssignmentNames().subscribe(data => {
      this.setAssignments(data);
    })
    this.testService.hasStudentSubmitted().subscribe(data => {
     this.hasSubmitted = data;

     if (!this.hasSubmitted['submitted']){
       alert("student has not submitted their assignment");
     }
    })
  }
  setCommentList (x:any){
    this.commentList = x;
  }

  setBehaviourList (x:any){
    this.behaviourType = x;
  }

  setBehaviourReport(a: any){
    this.behaviourReport = a;
  }

  updateCommentList(x:any, name:any){
     if (Object.keys(this.commentList).length <= this.studentLength){
        this.commentList[name] = x;
    }
  }

   updateBehaviourType(x:any, name:any){
     if (Object.keys(this.behaviourType).length <= this.studentLength) {
       this.behaviourType[name] = x;
     }
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
      this.sendBehaviour();
    });
  }

  getReport(){
    this.testService.fetchReport().subscribe(data => {
       this.testService.setReport(data);
       this.report = this.testService.getReport();
    })
  }

  getBehaviourReport(){
    this.testService.fetchBehaviourReport().subscribe(data => {
        this.setBehaviourReport(data);
    })
  }

  setClass(x: any){
    this.testService.setClass(x);
      this.testService.fetchClassData().subscribe(data => {
        this.testService.setData(data);
        this.dataClass = this.testService.getData();
        this.studentList = this.testService.getStudentData();
        this.createDefaults(this.studentList);
        this.testService.setStudent(this.studentList[0]);
        this.studentLength = this.studentList.length;
        this.getAssignmentNames();
      }
    )
  }

  setStudent(x:any){
    this.testService.setStudent(x);
  }
  title = 'Student Monitoring App';
}
