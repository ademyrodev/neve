# Neve.

> The perfect language for your side projects.

Neve is a high-level compiled language that aims to provide 
productivity, simplicity, speed and maintainability through its 
syntax and design philosophy.

Here’s your typical peek:
```rb
class LinkedNode
  value Int
  next LinkedNode?

  fun LinkedNode.new(value Int)
    LinkedNode with
      value = value
      next = nil
    end
  end
end

fun main
  let linked_list = LinkedNode.new -1

  10.times |i| do
    linked_list.next = LinkedNode.new i 
    linked_list = linked_list.next
  end
end
```

**Neve is still under construction!**

## What happened to “the old Neve?”

I decided to basically rework Neve from the ground up because 
the demand for low-level languages is already saturated.  You’ve
got C, Rust, Zig, and the list goes on.  Moreover, I myself 
wasn’t really satisfied with Neve.  I didn’t want a Rust clone 
and was looking for a programming language that would be 
delightful to both write **and** read, while also making me 
productive.

People today seem to value simplicity a lot, and so I decided to 
make Neve simpler.  People want to write both functional and 
imperative code, so I decided to make Neve a hybrid language.  
People want to write less, read less, and want their programs to
be faster, so I decided to work on Neve.

Today, it’s possible to make a language that meets those 
criteria.  Sure, most of those languages tend to be slept on, 
like Nim and Crystal, and that’s okay.  As long as it exists, 
there will be people to take a look at it.

# Pronunciation.

Don’t ask why this part was included.
English [nɪv]; Portuguese [ˈnε.vi]
