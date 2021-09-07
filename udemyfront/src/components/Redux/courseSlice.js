import { createAsyncThunk, createSlice } from '@reduxjs/toolkit'

const initialState = {
  course : [],
  status:"None",
  category:[]
}

const urlr ='http://127.0.0.1:8000/api/'

const url ='https://freeudemycourses.herokuapp.com/api/'


export const fetchCourses = createAsyncThunk(
  'courses/fetchall',
  async () => {
    const response = await fetch(`${url}`).catch(err=>console.log("we have  error",err))
    return response.json()
  }
)

export const fetchByCategory=createAsyncThunk(
  'courses/category',
  async(url_link)=>{
    const res = await fetch(`${url}${url_link}`).catch(err=>console.log("error while fetching category",err))
    return res.json()
  }
)
export const courseSlice = createSlice({
  name: 'course',
  initialState,
  reducers: {

  },
  extraReducers : {
    [fetchCourses.pending] : (state)=>{
        state.status = 'pending'
    },
    [fetchCourses.fulfilled] : (state,action)=>{
        state.status = 'fulfilled'
        state.course = action.payload
      
    },
    [fetchCourses.rejected] :(state,action)=>{
        state.status = 'rejected'
    },
    [fetchByCategory.pending]:(state)=>{
      state.status = 'pending'
    },
    [fetchByCategory.fulfilled]:(state,action)=>{
      state.status = 'fulfilled'
      state.category = action.payload
    },
    [fetchByCategory.rejected]:(state)=>{
      state.status = 'rejected'
    }
}
})

// Action creators are generated for each case reducer function
export const { increment, incrementByAmount } = courseSlice.actions

export default courseSlice.reducer