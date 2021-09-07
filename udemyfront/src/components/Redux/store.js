import { configureStore } from '@reduxjs/toolkit'
import counterSlice from './courseSlice'

export const store = configureStore({
  reducer: {
      courses : counterSlice
  },
})