import { Component, OnInit } from '@angular/core';
import { BookService } from '../book.service';
import { CommonModule, DecimalPipe } from '@angular/common';
import { RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-book-list',
  standalone: true,
  imports: [CommonModule, RouterModule, FormsModule],
  templateUrl: './book-list.component.html',
  styleUrl: './book-list.component.css',
  providers: []
})
export class BookListComponent implements OnInit {
  books: any[] = [];
  searchCriteria: string = 'title'; 

  constructor(private bookService: BookService) { 
  }

  ngOnInit(): void {
    this.bookService.getBooks().subscribe(data => {
      this.books = data;
      console.log(this.books);
    });
    
  }

  onSearch(event: KeyboardEvent): void {
    const inputElement = event.target as HTMLInputElement;
    const query = inputElement.value;

    if (event.key === 'Enter') {
      this.bookService.searchBooks(this.searchCriteria, query).subscribe(data => {
        this.books = data;
      });
    }
  }

}
