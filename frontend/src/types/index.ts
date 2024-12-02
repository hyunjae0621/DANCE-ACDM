// frontend/src/types/index.ts
export interface User {
  id: number;
  username: string;
  email: string;
  userType: 'admin' | 'teacher' | 'student';
}

export interface AuthState {
  user: User | null;
  isAuthenticated: boolean;
  loading: boolean;
}
