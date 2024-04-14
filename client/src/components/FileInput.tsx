import { useEffect, useState } from 'react';
import Dropzone, {useDropzone} from 'react-dropzone';

const  FileInput = ()=>{
   const {acceptedFiles, getRootProps, getInputProps} = useDropzone({
     accept:{
      "text":['.pdf']
     }
   });
   const [filename,setFilename] = useState<string>()
   useEffect(()=>{
      if(acceptedFiles.length!==0){
        console.log(acceptedFiles[0].name)
        setFilename(acceptedFiles[0].name)
      }
   },[acceptedFiles])
  return (
    <section className="h-7 ">
      <div {...getRootProps({className:"w-[70%] h-72  mx-auto border-dashed border-2 border-gray-200"})}>
        <input {...getInputProps()} />
        <p className='text-xl text-center mt-28'>{filename ? `${filename}` : 'Drag and drop a pdf or click to upload' }</p>
         {filename && <p className='text-xl text-center mt-10 underline underline-offset-3'>or try another file</p>}
      </div>
      {/* <aside>
        <h4>Files</h4>
        <ul>{files}</ul>
      </aside> */}
    </section>
  )
}

export default FileInput