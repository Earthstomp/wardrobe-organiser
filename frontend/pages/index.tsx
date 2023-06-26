import Image from 'next/image'
import { Inter } from 'next/font/google'

const inter = Inter({ subsets: ['latin'] })

export default function Home({ data, done }) {
  console.log('data: >> ', data);
  console.log('data: >> ', done);

  return (
    <>
      <p>Clothes</p>
      {data.map((element) =>
        <div key={element.slug}>
          <div>
            <img src={"https://res.cloudinary.com/dt2nnnvpe/" + element.image} height={120} width={120} alt="Clothing Image" />
          </div>
          <div>
            <h1>{element.title}</h1>
            <p>{element.description}</p>
            <p>{element.created_at}</p>
          </div>
        </div>)}
    </>
  )
}

// fetches at build time
export async function getStaticProps() {
  const response = await fetch("http://localhost:8000/api/clothes")

  const data = await response.json()

  return {
    props: {
      data: data,
      done: true,
    }
  }
}
